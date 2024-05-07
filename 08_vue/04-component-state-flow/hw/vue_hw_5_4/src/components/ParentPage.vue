<template>
  <div>
    <h1>부모 페이지입니다.</h1>
    <ChildPage
      v-for="child in children"
      :key="id"
      @update-balance="updateBalance(child)"
      :childProps="child"
    />
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import ChildPage from '@/components/ChildPage.vue'
  let id = 0
  const children = ref([
    {id:id++, name: '김하나', age: 30, balance: 100000},
    {id:id++, name: '김두리', age: 20, balance: 10000},
    {id:id++, name: '김서이', age: 10, balance: 1000}
  ]
)
  const updateBalance = function(child) {
    child.balance += 1000
  }

</script>

<style scoped>

</style>