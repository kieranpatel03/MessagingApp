import { createRouter, createWebHistory } from 'vue-router'
import MainApp from '../views/main.vue'
import MessageList from '../views/messages.vue'
import LoginPage from '../views/login.vue'
import SignupPage from '../views/signup.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: MainApp
  },
  {
    path: '/messages/:id',
    name: 'messages',
    component: MessageList,
  },
  { 
    path: '/login',
    name: 'login',
    component: LoginPage,
  },
  { path: '/signup',
    name: 'signup',
    component: SignupPage
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
