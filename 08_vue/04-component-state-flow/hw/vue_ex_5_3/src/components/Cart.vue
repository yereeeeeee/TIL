<template>
  <div>
    <li>
      {{ item.name }} - {{ item.price }}원
      <button @click="deleteToCart(item)">삭제</button>
    </li>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  defineProps({
    item: Object
  })

  const emit = defineEmits(['deleteToCart'])
  const deleteToCart = function (item) {
    emit('deleteToCart', item)
  }

</script>

<style scoped>

</style>