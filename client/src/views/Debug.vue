<template>
  <div class="container">
    <card
      v-for="card in cards"
      :key="card.id"
      :source="source"
      :rect="card.coords"
      :date="getDate(card.datetime)"
      :rating="Math.floor(card.rating)"
    />
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, ref } from "vue";
import Card from "@/components/Card.vue";
import axios from "axios";
import moment from "moment";

export default defineComponent({
  name: "Debug",
  components: {
    Card,
  },
  setup() {
    const cards = ref([]);

    const source = ref("");

    const getData = () => {
      axios.get("http://127.0.0.1:5000/detect").then((resp) => {
        cards.value = resp.data.data.clients.filter(
          (client: any) => client.id === 0
        );
        source.value = resp.data.data.source_image_base_64;
      });
    };

    getData();

    const current = ref(0);
    const prev = computed(() => {
      if (current.value === 0) return cards.value.length - 1;
      return current.value - 1;
    });

    const next = computed(() => {
      if (current.value === cards.value.length - 1) return 0;
      return current.value + 1;
    });

    const getDate = (datetime: string) => {
      return moment(datetime, "MM/DD/YYYY, h:mm a").format("DD.MM.YYYY");
    };

    setInterval(() => {
      current.value++;
      if (current.value === cards.value.length) {
        current.value = 0;
      }
    }, 4000);

    return {
      cards,
      current,
      prev,
      next,
      source,
      getDate,
    };
  },
});
</script>

<style scoped lang="scss"></style>
