const p1Img = document.querySelector('#player1-img')

const scissorsButton = document.querySelector('#scissors-button')
const rockButton = document.querySelector('#rock-button')
const paperButton = document.querySelector('#paper-button')

let countA = document.querySelector('.countA')
let countB = document.querySelector('.countB')
const playGame = function (player1, player2) {
  if (player1 == 'scissors') {
    if (player2 == 'rock') {
      countB.textContent = Number(countB.textContent) + 1
      return 2
    } else if (player2 == 'paper') {
      countA.textContent = Number(countA.textContent) + 1
      return 1
    }
  } else if (player1 == 'rock') {
    if (player2 == 'scissors') {
      countA.textContent = Number(countA.textContent) + 1
      return 1
    } else if (player2 == 'paper') {
      countB.textContent = Number(countB.textContent) + 1
      return 2
    }
  } else if (player1 == 'paper') {
    if (player2 == 'rock') {
      countA.textContent = Number(countA.textContent) + 1
      return 1
    } else if (player2 == 'scissors') {
      countB.textContent = Number(countB.textContent) + 1
      return 2
    }
  } else {
    return 0
  }
}

const resultPrint = document.querySelector('.modal-content')
const buttonClickHandler = function (choice) {
  p1Img.setAttribute('src', `./img/${choice}.png`)

  scissorsButton.setAttribute("disabled", "")
  rockButton.setAttribute("disabled", "")
  paperButton.setAttribute("disabled", "")

  const rspChoices = ['scissors', 'rock', 'paper']
  const p2Img = document.querySelector('#player2-img')
  let idx
  let rdm = setInterval(function() {
    idx = Math.round(Math.random()*2)
    p2Img.setAttribute('src', `./img/${rspChoices[idx]}.png`)
  }, 100)
  setTimeout(() => {
    clearInterval(rdm)
    const result = playGame(choice, rspChoices[idx])
    const modal = document.querySelector('.modal')
    modal.style.display = "flex"
    if (result === 1){
      resultPrint.textContent = 'Player 1 wins !'
    } else if (result === 2) {
      resultPrint.textContent = 'Player 2 wins !'
    } else {
      resultPrint.textContent = "It's a tie !"
    }
    setTimeout(() => {
      modal.style.display = 'none'
    }, 3000);
    scissorsButton.disabled = false
    rockButton.disabled = false
    paperButton.disabled = false
  },3000)
}
scissorsButton.addEventListener('click', () => {buttonClickHandler('scissors')})
rockButton.addEventListener('click', () => {buttonClickHandler('rock')})
paperButton.addEventListener('click', () => {buttonClickHandler('paper')})

