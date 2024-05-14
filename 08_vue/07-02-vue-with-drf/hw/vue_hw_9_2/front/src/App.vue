<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink> | 
        <RouterLink :to="{name:'SignUp'}">SignUp</RouterLink> | 
        <RouterLink :to="{name:'LogIn'}">SignIn</RouterLink> | 
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
</style>
