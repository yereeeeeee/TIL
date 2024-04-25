/* 
  아래에 코드를 작성해주세요.
*/

const fetchAlbums = function(page=1, limit=10) {
  // alert('확인!')
  axios({
    method:'get',
    url: 'https://ws.audioscrobbler.com/2.0/',
    params: {
      method:'artist.gettopalbums',
      page: page,
      limit: limit,
      artist: keyword,
      api_key: '###',
      format: 'json',
    },
  })
    .then((response) => {
      const albums = response.data.topalbums.album
      const result = document.querySelector('.search-result')
      result.textContent = ''
      // console.log(albums)
      albums.forEach(album => {

        const cardImg = document.createElement('img')
        cardImg.src = album.image[1]['#text']
        const text = document.createElement('div')
        text.classList.add('search-result__text')
        
        const artistTitle = document.createElement('h2')
        artistTitle.textContent = album.artist.name
        const albumTitle = document.createElement('p')
        albumTitle.textContent = album.name

        text.append(artistTitle)
        text.append(albumTitle)

        const card = document.createElement('div')
        card.classList.add('search-result__card')

        card.append(cardImg)
        card.append(text)

        const aTag = document.createElement('a')
        aTag.style.textDecoration = 'none'
        aTag.style.color = 'black'
        aTag.href = album.url
        aTag.append(card)
        
        result.appendChild(aTag)
      })

    })
    .catch((error) => {
      alert('잠시 후 다시 시도해주세요.')
      console.log(error)
    })
}

const inputSearch = document.querySelector('.search-box__input')
let keyword
const searchBtn = document.querySelector('.search-box__button')
searchBtn.addEventListener('click', function(event) {
  keyword = inputSearch.value
  fetchAlbums()
})