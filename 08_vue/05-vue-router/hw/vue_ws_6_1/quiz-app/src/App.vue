<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header class="main-header">
    <div class="header-background">
      <div class="card-div">
        <div class="card shadow-sm">
          <h5 class="card-header card-header-plus">Quiz 퀴즈</h5>
          <div class="card-body">
            <p class="card-text card-text-plus">여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요. 지금 바로 도전해보세요!</p>
          </div>
        </div>
      </div> 
      
      <div class="header-home-button-wrap">
        <button class="home-button">Home |</button>
      </div>
    </div>
  </header>

  <RouterView />
  <br><br>
</template>

<style scoped>
  .main-header {
    justify-content: center; 
    width:100%; 
    display: flex; 
    padding: 20px
  }
  .header-background {
    background-color: rgba(211, 211, 211, 0.288); 
    width: 100%; 
    justify-content: center; 
    padding: 20px; 
    width: max-content;
  }
  .card-div {
    width: fit-content; 
    text-align: center; 
    align-items: center;
  }
  .card-header-plus {
    background-color: rgb(255, 136, 0); 
    color: white; 
    font-weight: bolder; 
    padding: 20px 0; 
    font-size: x-large;
  }
  .card-text-plus {
    padding: 30px 20px; 
    font-weight: bold;
  }
  .header-home-button-wrap {
    margin-top: 30px;    
  }
  .home-button {
    width: 100%;
    background-color: rgb(36, 36, 36);
    color: white;
    padding: 5px 0;
    font-weight: bold;
  }
</style>
