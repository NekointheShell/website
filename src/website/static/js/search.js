function search(input) {
    event.preventDefault()

    cards = document.getElementsByClassName('card')
    for(card in cards) {
        try {
            if(!cards[card].innerText.includes(input)) {
                cards[card].style.display = 'none'
            }
            else {
                cards[card].style.display = ''
            }
        } catch(err) { true }
    }
}
