attributes_app = new Vue({
    el: '#attributes-container',
    delimiters: ['${','}'],
    data: {
    attributes: [],
    loading: false,
    currentAttribute: {},
    message: null,
    newAttribute: { 'name': null, 'datatype': null },
  },
  mounted: function() {
      this.getAttributes()
 },
  methods: {
      getAttributes: function() {
          this.loading = true;
          this.$http.get('/api/eav_attributes/')
              .then((response) => {
                this.attributes = response.data;
                risks_types_app.attributes = this.attributes;
                this.loading = false;
              })
              .catch((err) => {
               this.loading = false;
               console.log(err);
              })
      },
      addAttribute: function() {
          this.loading = true;
          this.$http.post('/api/eav_attributes/',this.newAttribute, {headers: {"X-CSRFToken":csrftoken }})
              .then((response) => {
                this.loading = false;
                this.getAttributes();
                $("#addAttributeModal").modal('toggle');
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
      },
      deleteAttribute: function(attribute_id) {
          this.loading = true;
          this.$http.delete('/api/eav_attributes/'+ attribute_id + '/', {headers: {"X-CSRFToken":csrftoken }})
              .then((response) => {
                  this.loading = false;
                  this.getAttributes();
              })
              .catch((err) => {
                  this.loading = false;
                  console.log(err);
              })
      }
 }
  });