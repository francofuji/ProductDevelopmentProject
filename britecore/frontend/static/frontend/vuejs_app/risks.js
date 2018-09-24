risks_app = new Vue({
    el: '#risks-container',
    delimiters: ['${','}'],
    data: {
    risks: [],
    risks_types: [],
    risk_type_attributes: [],
    loading: false,
    currentRisk: {},
    message: null,
    newRisk: { 'name': null, 'type': null, 'attributes': [] },
  },
  mounted: function() {
      this.getRisks();
      this.getRisks_Types();
 },
  methods: {
      changeRiskType: function() {
          var risk_type_id = $("#risk_type").val();
          this.$http.get('/api/risks_types/' + risk_type_id + '/')
              .then((response) => {
                  this.risk_type_attributes = response.data.attributes_details;
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
               })
      },
      getRisks: function() {
          this.loading = true;
          this.$http.get('/api/risks/')
              .then((response) => {
                this.risks = response.data;
                this.loading = false;
              })
              .catch((err) => {
               this.loading = false;
               console.log(err);
              })
      },
      getRisks_Types: function() {
        this.$http.get('/api/risks_types/')
            .then((response) => {
              this.risks_types = response.data;
            })
            .catch((err) => {
             this.loading = false;
             console.log(err);
            })
      },
      addRisk: function() {
          this.loading = true;
          this.newRisk['attributes'] = [];
          var nthis = this;
          $(".risk_attribute").each(function(){
              var nattribute = {"attribute_type": $(this).attr('id'), "value": $(this).val()};
              nthis.newRisk['attributes'].push(nattribute);
          });
          this.$http.post('/api/risks/',this.newRisk, {headers: {"X-CSRFToken":csrftoken }})
              .then((response) => {
                this.loading = false;
                this.getRisks();
                $("#addRiskModal").modal('toggle');
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
      },
      deleteRisk: function(risk_id) {
          this.loading = true;
          this.$http.delete('/api/risks/'+ risk_id + '/', {headers: {"X-CSRFToken":csrftoken }})
              .then((response) => {
                  this.loading = false;
                  this.getRisks();
              })
              .catch((err) => {
                  this.loading = false;
                  console.log(err);
              })
      }
 }
  });