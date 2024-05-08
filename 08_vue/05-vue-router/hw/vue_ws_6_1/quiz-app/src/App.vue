<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header style="justify-content: center; width:100%; display: flex; padding: 20px">
    <div style="background-color: rgba(211, 211, 211, 0.288); width: 100%; justify-content: center; display: flex; padding: 20px; width: max-content">
      <div style="width: fit-content; display: flex; text-align: center; align-items: center;">
        <div class="card shadow-sm" style="width: max-content%;">
          <h5 class="card-header" style="background-color: rgb(255, 136, 0); color: white; font-weight: bolder; padding: 20px 0; font-size: x-large;">Quiz 퀴즈</h5>
          <div class="card-body">
            <p class="card-text" style="padding: 30px 20px; font-weight: bold;">여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요. 지금 바로 도전해보세요!</p>
          </div>
        </div>
      </div>    
    </div>
  </header>



  <!-- <RouterView /> -->
</template>

<style scoped>
</style>
