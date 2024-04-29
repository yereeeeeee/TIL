/* 
  아래에 코드를 작성해주세요.
*/

const fetchAlbums = function(page=1, limit=10) {
  const loaderBox = document.querySelector('.search-result--loadingList')
  loaderBox.style.display = 'block'

  axios({
    method:'get',
    url: 'https://ws.audioscrobbler.com/2.0/',
    params: {
      method:'artist.gettopalbums',
      page: page,
      limit: limit,
      artist: keyword,
      api_key: 'dd21427ff35589664dffbaa0749eaf4d',
      format: 'json',
    },
  })
    .then((response) => {
      loaderBox.style.display = 'none'
      const albums = response.data.topalbums.album
    
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

      result.append(sentinel)

    })
    .catch((error) => {
      alert('잠시 후 다시 시도해주세요.')
      console.log(error)
    })
}

const inputSearch = document.querySelector('.search-box__input')

let keyword

const result = document.querySelector('.search-result')
let page = 1
let limit = 100

// 무한 스크롤 기준점 div
const sentinel = document.createElement('div')
sentinel.id = 'sentinel'
createObserver(sentinel)

const searchBtn = document.querySelector('.search-box__button')
searchBtn.addEventListener('click', function(event) {
  keyword = inputSearch.value
  result.textContent = ''
  fetchAlbums()
})

function createObserver(target) {
  const getMoreAlbums = (entries) => {
    entries.forEach(entrie => {
      if (entrie.isIntersecting) {
        page += 1
        fetchAlbums(page)
      }
    })
  }
  
  const observer = new IntersectionObserver(getMoreAlbums);
  observer.observe(target); 
}