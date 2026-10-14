<script setup>
import { computed } from "vue";
import UnitTable from "./UnitTable.vue";
import { dataLabel } from "@/assets/data-labels.js";

// The page owns its column order, headings and links; the source owns values.
const props = defineProps({
    data: { type: Object, required: true },
    columns: { type: Array, required: true },
    tableExtraInfo: { type: Array, default: () => [] },
    links: { type: Object, default: () => ({}) }
});
const table = computed(() => {
    const matches = props.data.tables.filter(table => props.columns.every(column => table.headers.includes(column.source)));
    if (matches.length !== 1) throw new Error(`${props.data.unitId}: expected one table matching the authored columns`);
    return matches[0];
});
const rows = computed(() => table.value.rows.map(row => props.columns.map(column => row[table.value.headers.indexOf(column.source)])));
function display(cell) {
    if (cell.status === "not_applicable") return "\\";
    if (cell.status === "unknown") return "未知";
    return cell.displayInput ?? (typeof cell.value === "number" ? String(cell.value) : dataLabel(cell.raw));
}
</script>

<template>
    <UnitTable :tableExtraInfo="tableExtraInfo">
        <table>
            <thead><tr><th v-for="column in columns" :key="column.source" v-html="column.heading" /></tr></thead>
            <tbody>
                <tr v-for="(row, index) in rows" :key="index">
                    <td v-for="(cell, column) in row" :key="column">
                        <a v-if="links[cell.raw]" :href="links[cell.raw]">{{ display(cell) }}</a>
                        <template v-else>{{ display(cell) }}</template>
                    </td>
                </tr>
            </tbody>
        </table>
    </UnitTable>
</template>
