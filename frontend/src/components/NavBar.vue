<template>
    <v-app-bar
      clipped-left
      clipped-right
      app
    >
      <!-- <v-app-bar-nav-icon
        v-if="primaryDrawer.type !== 'permanent'"
        @click.stop="primaryDrawer.model = !primaryDrawer.model"
      /> -->
<!-- 
          v-model="select"
          :loading="loading"
          :items="items"
          :search-input.sync="search" -->

      <v-toolbar-title >
        <router-link to="/"><h1 class="logo">Dark Notes</h1></router-link></v-toolbar-title>
          <v-autocomplete
          cache-items
          v-model="courseID"
          :items="courseList"
          item-text="name"
          item-value="code"
          :search-input.sync="search"
          :loading="isLoading"
          class="mx-4"
          hide-no-data
          hide-details
          label="Search courses"
          solo-inverted
        ></v-autocomplete>
        <v-btn large color="primary" text>About</v-btn>
        <v-btn large class="ml-2" v-if="!isLoggedIn" to="/login" color="primary">Login</v-btn>
        <v-btn large class="ml-2" v-else @click="logout" color="primary">Logout</v-btn>
    </v-app-bar>
</template>
<script>
import axios from 'axios'
export default {
    name: "NavBar",
    data() {
      return {
        courseList: [],
        isLoading: false,
        search: null,
        courseID: null
      }
    },
    computed: {
      isLoggedIn() { return this.$store.getters['auth/isLoggedIn'] }
    },
    methods: {
      logout() { return this.$store.dispatch('auth/logout')},
    },
    watch: {
      courseID(v) { this.$router.push(`/c/${v}`) },
      search() {
        if (this.courseList.length > 0) return
        if (this.isLoading) return
        this.isLoading = true

        axios.get('/courses/all')
        .then(r => {
          this.courseList = r.data.payload.map(e => {
            e.name = `${e.code} - ${e.name}`
            return e
          })
          this.isLoading = false
          console.log(this.courseList) //eslint-disable-line
        })
      }
    }

}
</script>
<style lang="scss">
.logo {
  color: #f35626;
  font-size: 2rem;
  background-image: linear-gradient(92deg, #f35626 0%,#feab3a 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: hue 60s infinite linear; 
}
.logo:hover {
  animation: hue 2s infinite linear; 
}
@keyframes hue {
  0% {
    filter: hue-rotate(0deg);
  }
  100% {
    filter: hue-rotate(-360deg);
  }
  
}
a {
  text-decoration: none;
}
</style>
