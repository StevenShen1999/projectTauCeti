
<template>
    
        <v-navigation-drawer 
        permanent
        :mini-variant.sync="mini"
        app
        clipped
        >
            <v-list-item two-line class="px-2">
                    <v-list-item-avatar>
                    <img src="https://randomuser.me/api/portraits/men/81.jpg">
                    </v-list-item-avatar>
                <v-list-item-content>
                    <v-list-item-title> COMP 1511 </v-list-item-title>
                    <v-list-item-subtitle> Fundamentals of programming </v-list-item-subtitle>
                </v-list-item-content>
                        <v-btn
                    icon
                    @click.stop="mini = !mini"
                    >
                    <v-icon>mdi-chevron-left</v-icon>
                    </v-btn>
            </v-list-item>
            <v-divider></v-divider>
            <v-list-item-group
            v-model="model" @change="changeTab" 
            dense
            nav
             mandatory
            >
                <v-list-item
                v-for="item in items"
                :key="item.title"
                link
                >
                <v-list-item-icon>
                    <v-icon>{{ item.icon }}</v-icon>
                </v-list-item-icon>

                <v-list-item-content>
                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item-content>
                </v-list-item>
            </v-list-item-group>
        </v-navigation-drawer>
</template>
<script>
export default {
    name: "CourseMenu",
    props: [
        'items'
    ],
    data: () => { return {
        model: null,
        mini: true
    }},
    methods: {
        changeTab(event) {
            this.$emit('input', event)
        }
    }

    
}
</script>
