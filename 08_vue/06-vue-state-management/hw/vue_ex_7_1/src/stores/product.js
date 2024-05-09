import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('product', () => {
  const products = ref([
    { id: 1, title: 'Product 1', body: 'quia' },
    { id: 2, title: 'Product 2', body: 'quo' },
    { id: 3, title: 'Product 3', body: 'repud' },
  ])

  return { products }
})
