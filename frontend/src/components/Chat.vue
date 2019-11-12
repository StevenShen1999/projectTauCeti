<template>
    <div class="wrapper">
        <div class="header" >
            <h2>
            Chat for COMP1511
            </h2>
        </div>
        <div class="messages">
            <p :class="index % 2 ? 'left' : 'right'" v-for="(message, index) in messages" :key="index">
                <b>{{message.user}}</b>: 
                {{message.message}}
            </p>
        </div>
        <div class="input">
            <form @submit="sendMessage">
            <input v-model="messageEntered" type="text" name="message"/>
            </form>
        </div>
        
    </div>
</template>
<script>
export default {
    data: () => ({
        messages: [
            { 
                message: "If you have one bucket that contains 2 gallons and another bucket that contains 7 gallons, how many buckets do you have?",
                user: "me"
            },

            { 
                message: "stfu",
                user: "u"
            },
        ], 
        messageEntered: ''
    }),
    methods: {
        sendMessage: function(e ) {
            e.preventDefault()
            this.messages.push(this.messageEntered)
            this.messageEntered = ""
        }
    }
}
</script>
<style lang="scss" scoped>
.wrapper {
    display: flex;
    width: 100%;
    height: 100%;
    position: relative;
    flex-direction: column;
    align-items: stretch;
}
.header {
    background-color: #FAFFD1;
    height: 50px;
    flex-grow: 0;
    text-align: center;
    position: relative;
    & h2 {
        position: absolute;
        width: 100%;
        bottom: 10px;
        margin: 0;
    }
}
.messages {
    flex-grow: 1;
    position: relative;
    display: flex;
    flex-direction: column;
}
p {
    margin: 5px;
    margin-left: 1rem;
    font-size: .8rem;
}
.input {
    position: relative;
    & form {
        position: relative;
    }
    & input {
        width: 100%;
        padding: 1em 1.5em;
        border: none;
        background-color: #eee;
    }
}

</style>