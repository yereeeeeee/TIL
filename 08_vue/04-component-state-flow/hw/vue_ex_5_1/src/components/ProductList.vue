<template>
  <div>
    <li>{{ product.name }} - {{ product.price }}원</li>
  </div>
</template>

<script setup>
  defineProps({
    product: Object
  })
</script>

<style lang="scss" scoped>

</style>