<template>
<div>
                <v-list>
                  <v-list-item>
                    <v-list-item-content>
                      <h1>Sign up</h1>
                      <p> Welcome!</p>
                      <p> Sign up to get access to all our notes!</p>
                  </v-list-item-content>
                  </v-list-item>
                  <v-form @submit="submitForm">
                  <v-list-item>
                    <v-text-field 
                      outlined
                    v-model="username" label="Username"></v-text-field>
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
                      :rules="password.rules"
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
                    <v-text-field
                      outlined
                      :append-icon="password.show ? 'mdi-eye' : 'mdi-eye-off'"
                      :rules="password.rules"
                      :type="password.show ? 'text' : 'password'"
                      name="input-10-2"
                      label="Confirm Password"
                      hint=""
                      v-model="newPassword.value"
                      class="input-group--focused"
                      @click:append="password.show = !password.show"
                    ></v-text-field>
                  </v-list-item>
                  </v-form>
                  <v-list-item>
                    Already registered? Log in <v-btn @click="$emit('change')"  small class="pa-0" text > here </v-btn>
                  </v-list-item>
                </v-list>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" @click="submitForm">Sign up</v-btn>
                  </v-card-actions>
                  </div>
</template>

<script>
// import { mapActions } from 'vuex'
export default {
    name: "SignUpForm",
    data: () => { return {
        newPassword: {
            value: "",
            show: false,
            rules: [
                value => !!value || "Required.",
                v => v.length >= 8 || "Min 8 characters",
            ]
        },
        email: "",
        username: "",
        password: {
            value: "",
            show: false,
            rules: [
              value => !!value || "Required.",
              v => v.length >= 8 || "Min 8 characters",
            ]
        },
        }
    },
    methods: {
      submitForm() {
        const data = {
          username: this.username,
          email: this.email,
          password: this.password.value
        }
        this.$store.dispatch('auth/register', data)
        .then(() => alert("YAY"))
        .catch(err => console.log(err))
      }
    }
}
</script>