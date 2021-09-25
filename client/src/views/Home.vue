<template>
  <div class="home">
    <div class="cards-container">
      <card v-for="card in cards" :key="card.id" :source="card.source" />
    </div>
    <div class="text">
      <div class="line">Их разыскивает Дед Мазай!!!</div>
      <div class="line">Их разыскивает Дед Мазай!!!</div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import Card from "../components/Card.vue";

export default defineComponent({
  name: "Home",
  components: {
    Card,
  },
  setup() {
    const cards = ref([
      {
        id: 1,
        source: "https://i.imgur.com/4eJioYc.png",
      },
      {
        id: 2,
        source: "https://i.imgur.com/4eJioYc.png",
      },
      {
        id: 3,
        source: "https://i.imgur.com/4eJioYc.png",
      },
    ]);

    const counter = ref(0);

    return {
      cards,
      counter,
    };
  },
});
</script>

<style scoped lang="scss">
.home {
  padding: 0;
  margin: 0;
  background-image: url("../assets/bg_1.svg");
  background-repeat: repeat-x;
  background-size: 115% 105%;
  height: 100%;
  width: 100%;
  display: grid;
  grid-template-areas:
    "cards"
    "text";
  grid-template-columns: 1fr;
  grid-template-rows: 1fr 200px;
}

.cards-container {
  padding-top: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
  grid-area: cards;
}

.text {
  grid-area: text;
  box-sizing: border-box;
  color: #fff;
  font-size: 71px;
  height: 200px;
  width: 100%;
  line-height: 200px;
  overflow: hidden;
  font-weight: bolder;
  text-align: left;
  position: relative;
  background: rgba(#000, 0.1);
  user-select: none;

  .line {
    text-shadow: 3px 1px 0  #000;
    right: -100%;
    top: 0;
    position: absolute;
    animation: RunningLine infinite 10s linear;
  }

  .line:last-child {
    animation: RunningLine infinite 10s 5s linear;
  }
}

@keyframes RunningLine {
  from {
    left: 100%;
  }
  to {
    left: -50%;
  }
}
</style>
