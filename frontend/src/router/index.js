import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import CreateView from '../views/CreateView.vue';
import GenerateView from '../views/GenerateView.vue';
import PlayView from '../views/PlayView.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/create',
    name: 'create',
    component: CreateView
  },
  {
    path: '/generate',
    name: 'generate',
    component: GenerateView
  },
  {
    path: '/play',
    name: 'play',
    component: PlayView
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;