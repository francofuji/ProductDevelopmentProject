Vue.component('risk_attribute_component', {
    props: ['risk_attribute'],
    template: '\
        <div class="form-group"> \
        <label>{{ risk_attribute.name }}</label>\
        <input type="text" v-bind:id="risk_attribute.id" class="form-control risk_attribute" required="required" v-if="risk_attribute.datatype===\'text\'"/> \
        <input type="date" v-bind:id="risk_attribute.id" class="form-control risk_attribute" required="required" v-if="risk_attribute.datatype===\'date\'"/> \
        <input type="number" v-bind:id="risk_attribute.id" class="form-control risk_attribute" required="required" v-if="risk_attribute.datatype===\'int\'"/> \
        <input type="number" v-bind:id="risk_attribute.id" class="form-control risk_attribute" required="required" v-if="risk_attribute.datatype===\'float\'"/> \
        </div> \
    '
});