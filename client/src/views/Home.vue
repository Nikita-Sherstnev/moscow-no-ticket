<template>
  <div class="home">
    <div class="cards-container">
      <!--      <card-->
      <!--        v-for="card in cards"-->
      <!--        :key="card.id"-->
      <!--        :source="card.source"-->
      <!--        :rect="card.rect"-->
      <!--      />-->
      <card
        :key="cards[prev].id"
        :source="cards[prev].source"
        :rect="cards[prev].rect"
      />
      <card
        :key="cards[current].id"
        :source="cards[current].source"
        :rect="cards[current].rect"
      />
      <card
        :key="cards[next].id"
        :source="cards[next].source"
        :rect="cards[next].rect"
      />
    </div>
    <div class="text">
      <div class="line">Их разыскивает Дед Мазай!!!</div>
      <div class="line">Их разыскивает Дед Мазай!!!</div>
    </div>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, ref } from "vue";
import Card from "../components/Card.vue";
import { useIntervalFn } from "@vueuse/core";

export default defineComponent({
  name: "Home",
  components: {
    Card,
  },
  setup() {
    // "https://i.imgur.com/4eJioYc.png",
    const cards = ref([
      {
        id: 1,
        source: "https://i.imgur.com/faOzV6y.jpg",
        rect: [904, 175, 939, 224],
      },
      {
        id: 2,
        source: "https://i.imgur.com/faOzV6y.jpg",
        rect: [445.14645, 173.83963, 479.26056, 221.26477],
      },
      {
        id: 3,
        source: "https://i.imgur.com/faOzV6y.jpg",
        rect: [871.2262, 65.61149, 895.45276, 91.72891],
      },
    ]);

    const current = ref(0);
    const prev = computed(() => {
      if (current.value === 0) return cards.value.length - 1;
      return current.value - 1;
    });
    const next = computed(() => {
      if (current.value === cards.value.length - 1) return 0;
      return current.value + 1;
    });

    setInterval(() => {
      current.value++;
      if (current.value === cards.value.length) {
        current.value = 0;
      }
    }, 1000);

    return {
      cards,
      current,
      prev,
      next,
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
  overflow: hidden;
}

.cards-container {
  padding-top: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.text {
  position: absolute;
  left: 0;
  bottom: 0;
  box-sizing: border-box;
  color: #fff;
  font-size: 71px;
  height: 200px;
  width: 100%;
  line-height: 200px;
  overflow: hidden;
  font-weight: bolder;
  text-align: left;
  background: rgba(#000, 0.1);
  user-select: none;
  font-family: Roboto, serif;
  z-index: 99999;

  .line {
    text-shadow: 3px 1px 0 #000;
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
