<template>
  <div>
    <h2>User Profile</h2>
    <p>Username: {{ username }}</p>
    <RouterLink :to="{ name:'user-profile' }">상세 프로필</RouterLink>
    <span> | </span>
    <RouterLink :to="{ name:'user-posts' }">작성한 게시글</RouterLink>
  </div>
  <hr>
  <RouterView />
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router';
import { RouterView } from 'vue-router';
import { useRoute } from 'vue-router'

const route = useRoute()
const username = ref(route.params.username)
</script>
