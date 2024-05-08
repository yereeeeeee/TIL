<template>
  <div>
    {{ product.name }} - {{ product.price }}원
    <button>장바구니 추가</button>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  defineProps({
    product: Object
  })
</script>

<style scoped>

</style>