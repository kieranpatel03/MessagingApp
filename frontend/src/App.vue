<template>
  <HeaderApp/>
  <router-view/>
</template>

<script>
import HeaderApp from "./components/header.vue"


export default {
    name: 'MainApp',
    components: {
        HeaderApp,
    }
}
</script>

<style>
body {
    background-color: #FFFDE4;
}
</style>
