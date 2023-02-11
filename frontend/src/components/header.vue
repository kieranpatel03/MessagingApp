<template>
    <div class='head_border'>
      <div class="inner-div">
        <h1 class='page_title'>Messager</h1>
        <div v-if="$cookies.get('token')" class="buttons">
          <span class="link-text" @click="log_out()"><h1>Log Out</h1></span>
        </div>
        <div v-else class="buttons">
          <router-link to='/login' class="link-text"><h1>Login</h1></router-link>
          <router-link to='/signup' class="link-text"><h1>Sign Up</h1></router-link>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: 'HeaderApp',
  methods: {
    log_out() {
      this.$cookies.set('token', '')
      this.$router.push('/').then(() => { this.$router.go() })
    }
  }
}
</script>

<style>
.head_border {
  height: 100px; 
  background-color: #7FFFD4;
  position: sticky;
  width: 100%;
  z-index: 1;
  text-align: center;
  justify-content: center;
}

.inner-div {
  position: relative;
  height: 100%;
}

.buttons {
  position: absolute;
  left: 75%;
  top: 0%;
  height: 100%;
  width: 20%;
  display: flex;
  justify-content: space-around;
}

.link-text {
  text-decoration: none;
  color: black;
  flex: 1;
  display: flex;
  justify-content: center;
}

.link-text:hover {
  background-color: #90EE90; 
}





.page_title {
  margin: 0;
  font-size: 50px;
  font-family: cursive;
  background: linear-gradient(90deg, #000000, #FEFBEA);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
</style>