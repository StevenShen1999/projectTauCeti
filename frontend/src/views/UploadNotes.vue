<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="6">
        <v-card max-width="700">
          <v-card-title>Login</v-card-title>
          <v-card-text>
            <v-text-field model="username" label="Username"></v-text-field>
            <v-text-field
              :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
              :rules="[password.rules.required, password.rules.min]"
              :type="password.show ? 'text' : 'password'"
              name="Password"
              label="Password"
              hint="At least 8 characters"
              model="password"
              class="input-group--focused"
              @click:append="password.show = !password.show"
            ></v-text-field>
            Not a member? Sign up <v-btn small class="pa-0" text > here </v-btn>
          </v-card-text>
          <v-card-actions>
              <v-spacer></v-spacer>
            <v-btn color="primary">Login</v-btn>

          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
    
</template>