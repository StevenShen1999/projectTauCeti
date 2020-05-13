<template>
  <v-container fluid class="fill-height background">
    <v-row justify="center" align="center">
      <v-col class="d-flex justify-center">
        <v-card max-width="700">
          <v-container fluid class="pa-0 overflow-hidden">
            <v-scroll-x-reverse-transition hide-on-leave>
              <v-row align="stretch" class="pa-0" v-if="loginPage">
                <v-col cols="6" class="pa-0">
                  <v-img
                    class="fill-height"
                    src="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"
                  />
                </v-col>
                <v-col cols="6">
                  <v-card-text>
                    <LoginForm @change="loginPage = !loginPage" />
                  </v-card-text>
                </v-col>
              </v-row>
            </v-scroll-x-reverse-transition>
            <v-scroll-x-transition hide-on-leave>
              <v-row align="stretch" class="pa-0" v-if="!loginPage">
                <v-col cols="6">
                  <v-card-text>
                    <SignupForm @change="loginPage = !loginPage" />
                  </v-card-text>
                </v-col>
                <v-col cols="6" class="pa-0">
                  <v-img
                    class="fill-height"
                    src="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/adorable-cavalier-king-charles-spaniel-puppy-royalty-free-image-523255012-1565106446.jpg?crop=0.448xw:1.00xh;0.370xw,0&resize=480:*"
                  />
                </v-col>
              </v-row>
            </v-scroll-x-transition>
          </v-container>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import LoginForm from "@/components/LoginForm.vue";
import SignupForm from "@/components/SignupForm.vue";
export default {
  name: "auth",
  components: {
    LoginForm,
    SignupForm
  },
  data: () => {
    return {
      loginPage: true
    };
  },
  methods: {
    login() {
      const data = {
        email: this.email,
        password: this.password.value
      };
      this.$store
        .dispatch("auth/login", data)
        .then(() => this.$outer.push("/"))
        .catch(e => console.log(e));
    }
  }
};
</script>
<style scoped>
.background {
  background: linear-gradient(to bottom right, #ffefba, #ffffff);
}
</style>