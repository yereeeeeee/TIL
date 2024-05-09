<template>
  <div>
    <h1>pinia 연습하기</h1>
  </div>

  <div class="main">
    <ParentPage 
      v-for="family in store.familyInfo"
      :family="family"
    />
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import ParentPage from './ParentPage.vue';
  import { useFamilyStore } from '@/stores/family';

  const store = useFamilyStore()

</script>

<style scoped>
  .main {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
</style>