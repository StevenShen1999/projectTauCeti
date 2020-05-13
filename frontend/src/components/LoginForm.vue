<template>
<div>
                <v-list>
                  <v-list-item>
                    <v-list-item-content>
                      <h1> Login </h1>
                      <p> Welcome back! </p>
                      <p> Log in to your account</p>
                  </v-list-item-content>
                  </v-list-item>
                  <v-list-item>
                    <v-text-field 
                      outlined
                    v-model="email" label="Email"></v-text-field>
                  </v-list-item>
                  <v-list-item>
                    <v-text-field
                      outlined
                      :append-icon="password.show ? 'mdi-eye' : 'mdi-eye-off'"
                      :rules="[password.rules.required, password.rules.min]"
                      :type="password.show ? 'text' : 'password'"
                      name="input-10-2"
                      label="Password"
                      hint=""
                      v-model="password.value"
                      class="input-group--focused"
                      @click:append="password.show = !password.show"
                    ></v-text-field>
                  </v-list-item>
                  <v-list-item>
                    Not a member? Sign up <v-btn small @click="$emit('change')" class="pa-0" text > here </v-btn>
                  </v-list-item>
                </v-list>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" @click="submitForm">Login</v-btn>
                  </v-card-actions>
                  </div>
</template>
<script>
export default {
  name: "LoginForm",
  data: () => {
    return {
      email: "",
      password: {
          value: "",
          show: false,
          rules: {
          required: value => !!value || "Required.",
          min: v => v.length >= 8 || "Min 8 characters",
          emailMatch: () => "The email and password you entered don't match"
          }
      },
    }
  },
  methods: {
    submitForm() {
      const data = {
        email: this.email,
        password: this.password.value
      }
      this.$store.dispatch('auth/login', data)
      .then(() => {
        this.$router.push('/')
      })
    }
  }

}
</script>