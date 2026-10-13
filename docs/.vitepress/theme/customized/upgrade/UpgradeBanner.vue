<script setup>
import { computed } from "vue";
import { availableTempUnits, availableCraftedBuildings, isTemporaryAvailable } from "#/global-variables.js";
import { isUpgradeDetails } from "@/assets/global/common.js";
import Callout from "@/components/Callout.vue";

const props = defineProps({
    link: {
        type: String,
        required: true
    }
});

const availableState = computed(() => {
    const result = {
        tempTroopAvailable: false,
        tempSpellAvailable: false,
        tempTrapAvailable: false,
        craftedBuildingAvailable: false
    };

    if (!props.link || !isUpgradeDetails(props.link)) {
        return result;
    }

    // 提取链接中的序号
    const unitId = props.link.substring(9, 13);

    // 判断是否为可用的临时单位
    const availableTempTroops = [];
    const availableTempSpells = [];
    const availableTempTraps = [];
    for (const availableItem of availableTempUnits.filter(item => isTemporaryAvailable(item))) {
        const prefix = availableItem.substring(0, 3);
        if (["0e0", "0e1", "0e2", "0e3", "0e4", "0e5", "0e6", "0e7"].includes(prefix)) {
            availableTempTroops.push(availableItem);
        } else if (["0e8", "0e9", "0ea", "0eb", "0ec", "0ed", "0ee", "0ef"].includes(prefix)) {
            availableTempSpells.push(availableItem);
        } else {
            availableTempTraps.push(availableItem);
        }
    }
    result.tempTroopAvailable = availableTempTroops.includes(unitId);
    result.tempSpellAvailable = availableTempSpells.includes(unitId);
    result.tempTrapAvailable = availableTempTraps.includes(unitId);
    
    // 判断是否为可用的精工防御
    result.craftedBuildingAvailable = availableCraftedBuildings.includes(unitId);

    return result;
});

const tempTroopAvailable = computed(() => availableState.value.tempTroopAvailable);
const tempSpellAvailable = computed(() => availableState.value.tempSpellAvailable);
const tempTrapAvailable = computed(() => availableState.value.tempTrapAvailable);
const craftedBuildingAvailable = computed(() => availableState.value.craftedBuildingAvailable);
</script>

<template>
    <Callout type="success" class="cp-callout-available-tip" v-if="tempTroopAvailable">
        该临时兵种本期活动可用（2026-10-08 至 2026-10-25）。在活动期间，你可以训练和使用该兵种。
    </Callout>
    <Callout type="success" class="cp-callout-available-tip" v-else-if="tempSpellAvailable">
        该临时法术现在可用。在活动期间，你可以配置和部署该法术。
    </Callout>
    <Callout type="success" class="cp-callout-available-tip" v-else-if="tempTrapAvailable">
        该临时陷阱现在可用。在活动期间，你可以购买和部署该陷阱。
    </Callout>
    <Callout type="success" class="cp-callout-available-tip" v-else-if="craftedBuildingAvailable">
        该精工防御属于 2026 年 8 月开放的批次（截至 2026-10-13）。新一批推出前可以升级该防御。
    </Callout>
</template>
