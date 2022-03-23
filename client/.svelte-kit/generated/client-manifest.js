export { matchers } from './client-matchers.js';

export const components = [
	() => import("..\\..\\src\\routes\\__layout.svelte"),
	() => import("..\\runtime\\components\\error.svelte"),
	() => import("..\\..\\src\\routes\\index.svelte"),
	() => import("..\\..\\src\\routes\\signup.svelte"),
	() => import("..\\..\\src\\routes\\login.svelte"),
	() => import("..\\..\\src\\routes\\chat\\[to].svelte"),
	() => import("..\\..\\src\\routes\\join.svelte"),
	() => import("..\\..\\src\\routes\\l.svelte")
];

export const dictionary = {
	"": [[0, 2], [1]],
	"signup": [[0, 3], [1]],
	"login": [[0, 4], [1]],
	"chat/[to]": [[0, 5], [1]],
	"join": [[0, 6], [1]],
	"l": [[0, 7], [1]]
};