new Vue({
    el: '#messages_app',
    data: {
        messages: []
    },
    created: function () {
        const vm = this;
        axios.get('/api/messages/')
            .then(function (response){
            vm.messages = response.data
        })
    }
})