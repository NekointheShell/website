from flask import Flask, request, render_template, send_from_directory
import pkgutil, yaml, markdown


app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('images/terminal.svg')


@app.route('/')
def root():
    feed = ''

    index = yaml.safe_load(pkgutil.get_data(__name__, 'posts/index.yml'))
    for entry in index:
        title = '<h1>{}</h1>'.format(entry['title'])

        if 'github' in entry: github = "<a href='{}'><img src='static/images/github.svg' alt='Github'></a>".format(entry['github'])
        else: github = ''

        text = '<p>{}</p>'.format(entry['text'])
        link = "<a href='posts/{}'>Read more...</a>".format(entry['link'])
        date = '<p>{}</p>'.format(entry['date'])

        card = """
            <link rel='stylesheet' href='static/css/card.css'>
            <section class='card'>
                <section class='title'>
                    {title}
                </section>

                <section class='github'>
                    {github}
                </section>

                <section class='text'>
                    {text}
                    {link}
                </section>

                <section class='date'>
                    {date}
                </section>
            </section>
        """.format(title=title, github=github, text=text, link=link, date=date)
        feed += card

    return render_template('feed.html', feed=feed)


@app.route('/posts/<page>')
def posts(page):
    index = yaml.safe_load(pkgutil.get_data(__name__, 'posts/index.yml'))
    for entry in index:
        if page == entry['link']:
            data = markdown.markdown(pkgutil.get_data(__name__, 'posts/{}.md'.format(entry['link'])).decode())
            return render_template('post.html', post=data)

    abort(404)


@app.route('/posts/images/<path:filename>')
def posts_images(filename):
    return send_from_directory('posts/images', filename)
