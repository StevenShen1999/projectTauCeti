<template>
  <v-app>
    <NavBar/>

    <v-content>
      <router-view> </router-view>

    </v-content>
      <!-- <v-footer
        app style="background:transparent"
      >
      <span class="px-4">&copy; {{ new Date().getFullYear() }}</span>
      </v-footer> -->
  </v-app>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
  export default {
    components: {
      NavBar
    },
    data: () => ({
      drawers: ['Default (no property)', 'Permanent', 'Temporary'],
      footer: {
        inset: false,
      },
    }),
  }
</script>
<style lang="scss" scoped>
* {
  box-sizing: border-box;
}
body {
  // font-family: $body-font-family, sans-serif !important; 
  margin: 0;
}
</style>
