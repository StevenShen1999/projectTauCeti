
<template>
    
            <v-card
            max-width="500"
            class="my-3"
            tile
            >
                <v-list
                three-line
                subheader
                >
                <v-list-item>
                    <v-list-item-title class="title">
                        Notes
                    </v-list-item-title>
                </v-list-item>
                            <v-list-item-group v-model="items" color="primary">
                    <v-list-item
                        v-for="(item, i) in items"
                        :key="i"
                    >
                        <!-- :inactive="inactive" -->
                        <v-list-item-avatar >
                        <v-img src="https://cdn.vuetifyjs.com/images/lists/3.jpg"></v-img>
                        </v-list-item-avatar>
                        <v-list-item-content>
      <v-list-item-content>
        <v-list-item-title>The best notes</v-list-item-title>
        <v-list-item-subtitle> It has pictures of bobs and vegene</v-list-item-subtitle>
        <v-list-item-subtitle>
            Take it
        </v-list-item-subtitle>
      </v-list-item-content>
                        </v-list-item-content>
                    </v-list-item>
                    </v-list-item-group>

                </v-list>
            </v-card>
</template>
<script>
export default {
    name: "CourseNotes",
    data: () => {
        return {

            items: [
                {
                icon: 'home',
                title: 'Home'
                },
                {
                icon: 'info',
                title: 'Course Information'
                },
                {
                icon: 'list',
                title: 'Notes'
                },
            ]
        }
    }
}
</script>