risks_types_app = new Vue({
    el: '#riskstypes-container',
    delimiters: ['${','}'],
    data: {
    risks_types: [],
    attributes: [],
    loading: false,
    currentRiskType: {},
    message: null,
    newRiskType: { 'name': null, 'attributes': [] },
  },
  mounted: function() {
      this.getRisksTypes();
      this.getAttributes();
 },
  methods: {
    getAttributes: function() {
        this.$http.get('/api/eav_attributes/')
            .then((response) => {
              this.attributes = response.data;
              this.loading = false;
            })
            .catch((err) => {
             console.log(err);
            })
    },
      getRisksTypes: function() {
          this.loading = true;
          this.$http.get('/api/risks_types/')
              .then((response) => {
                this.risks_types = response.data;
                this.loading = false;
              })
              .catch((err) => {
               this.loading = false;
               console.log(err);
              })
      },
      addRiskType: function() {
          this.loading = true;
          this.$http.post('/api/risks_types/',this.newRiskType, {headers: {"X-CSRFToken":csrftoken }})
              .then((response) => {
                this.loading = false;
                this.getRisksTypes();
                $("#addRiskTypeModal").modal('toggle');
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
      },
      deleteRiskType: function(risk_type_id) {
          this.loading = true;
          this.$http.delete('/api/risks_types/'+ risk_type_id + '/', {headers: {"X-CSRFToken":csrftoken }})
              .then((response) => {
                  this.loading = false;
                  this.getRisksTypes();
              })
              .catch((err) => {
                  this.loading = false;
                  console.log(err);
              })
      }
 }
  });