<template>
  <div>
    <h1>쇼핑 애플리케이션</h1>
    <ProductList :products="products" @add-to-cart="addToCart" />
  </div>
  <p>총 가격 : {{ totalPrice }}원</p>
  <div>
    <h1>장바구니</h1>
    <ul>
      <Cart
        v-for="item in items"
        :key="id"
        :item="item"
        @delete-to-cart="deleteToCart"
      />
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ProductList from '@/components/ProductList.vue'
import Cart from './components/Cart.vue';

let id = 0

const products = ref([
  { id: id++, name: '사과', price: 1000 },
  { id: id++, name: '바나나', price: 1500 },
  { id: id++, name: '딸기', price: 2000 },
  { id: id++, name: '포도', price: 3000 },
  { id: id++, name: '복숭아', price: 2000 },
  { id: id++, name: '수박', price: 5000 }
])

const totalPrice = ref(0)
const items = ref([])
let item_id = 0

const addToCart = function(product) {
  // console.log(id)
  items.value.push({
    id: item_id++,
    name: product.name,
    price: product.price, 
  })
 
  totalPrice.value += product.price
  // console.log(items)
}

const deleteToCart = function(item) {
  // console.log(item.id)
  totalPrice.value -= item.price
  
  const deleteItemId = items.value.findIndex(i => i.id == item.id)
  items.value.splice(deleteItemId, 1)

}

</script>
