bg="black"
fg="green"
active="white"

items = {
	"equipment" : {
		"main-hand" : {
			"rusty sword" : {
				"desc" : "A rusted sword. Nothing could be worse.",
				"stats" : {
					"strength" : 1,
					"dexterity" : 1,
					"wisdom" : 1,
					"vitality" : 1,
					"attack" : 10,
				},
				"value" : 3,
			},
			"stick" : {
				"desc" : "A stick. The wizard's emergency wand.",
				"stats" : {
					"strength" : 1,
					"dexterity" : 1,
					"wisdom" : 1,
					"vitality" : 1,
					"attack" : 10,
				},
				"value" : 3,
			},
			"children's bow" : {
				"desc" : "A bow for children.",
				"stats" : {
					"strength" : 1,
					"dexterity" : 1,
					"wisdom" : 1,
					"vitality" : 1,
					"attack" : 10,
				},
				"value" : 3,
			},
			"crude club" : {
				"desc" : "A log roughly the shape you'd expect a club to have.",
				"stats" : {
					"strength" : 1,
					"dexterity" : 1,
					"wisdom" : 1,
					"vitality" : 1,
					"attack" : 10,
				},
				"value" : 3,
			},
		},
		"off-hand" : {
			"buckler" : {
				"desc" : "A small wooden shield.",
				"stats" : {
					"strength" : 1,
					"dexterity" : 1,
					"wisdom" : 1,
					"vitality" : 1,
					"armor" : 10,
				},
				"value" : 3,
			},
		},
		"head" : {
			"bandana" : {
				"desc" : "A square cloth",
				"stats" : {
					"strength" : 1,
					"dexterity" : 1,
					"wisdom" : 1,
					"vitality" : 1,
					"armor" : 10,
				},
				"value" : 3,
			},
			"hood" : {
				"desc" : "A cloth hood.",
				"stats" : {
					"strength" : 1,
					"dexterity" : 1,
					"wisdom" : 1,
					"vitality" : 1,
					"armor" : 10,
				},
				"value" : 3,
			},
			"worn cowl" : {
				"desc" : "A leather cowl that has seen better days.",
				"stats" : {
					"strength" : 1,
					"dexterity" : 1,
					"wisdom" : 1,
					"vitality" : 1,
					"armor" : 10,
				},
				"value" : 3,
			},
			"cracked helmet" : {
				"desc" : "A cracked bronze helmet.",
				"stats" : {
					"strength" : 1,
					"dexterity" : 1,
					"wisdom" : 1,
					"vitality" : 1,
					"armor" : 10,
				},
				"value" : 3,
			},
		},
		"chest" : {
			"shirt" : {
				"desc" : "A simple cloth shirt.",
				"stats" : {
					"strength" : 1,
					"dexterity" : 1,
					"wisdom" : 1,
					"vitality" : 1,
					"armor" : 10,
				},
				"value" : 3,
			},
			"robe" : {
				"desc" : "A cloth robe.",
				"stats" : {
					"strength" : 1,
					"dexterity" : 1,
					"wisdom" : 1,
					"vitality" : 1,
					"armor" : 1,
				},
				"value" : 3,
			},
		},
		"legs" : {
			"battered clogs" : {
				"desc" : "There's a real splinter problem.",
				"stats" : {
					"strength" : 1,
					"dexterity" : 1,
					"wisdom" : 1,
					"vitality" : 1,
					"armor" : 1,
				},
				"value" : 3,
			},
		},
	},
	"consumables" : {
		"restoratives" : {
			"health potion" : {
				"desc" : "Restores health.",
				"use" : {
					"hp" : 10,
				},
				"value" : 3,
			},
		},
		"offensive" : {
			"fire bomb" : {
				"desc" : "A bomb that spews burning liquid all around it.",
				"use" : {},
				"value" : 3,
			},
		},
	},
	"key items" : {
		"quest" : {
			"golden apple" : {
				"desc" : "An apple made of solid gold.",
			},
		},
		"upgrades" : {
			"bronze pickaxe" : {
				"desc" : "With this I can mine for ores.",
			},
		},
	},
	"resources" : {
		"ores" : {
			"iron ore" : {
				"desc" : "A rock containing a high percentage of iron.",
				"xp" : 35,
				"level" : 15,
			},
			"copper ore" : {
				"desc" : "A rock containing a high percentage of copper.",
				"xp" : 5,
				"level" : 1,
			},
			"tin ore" : {
				"desc" : "A rock containing a high percentage of tin.",
				"xp" : 20,
				"level" : 10,
			},
			"zinc ore" : {
				"desc" : "A rock containing a high percentage of zinc.",
				"xp" : 10,
				"level" : 5,
			},
		},
		"ingots" : {
			"brass ingot" : {
				"desc" : "A refined bar of brass alloy",
				"xp" : 10,
				"level" : 5,
				"mats" : ["zinc ore","copper ore"],
			},
			"copper ingot" : {
				"desc" : "A refined bar of copper",
				"xp" : 5,
				"level" : 1,
				"mats" : ["copper ore"],
			},
			"bronze ingot" : {
				"desc" : "A refined bar of bronze alloy",
				"xp" : 20,
				"level" : 10,
				"mats" : ["copper ore","tin ore"],
			},
		},
		"fish" : {
			"bluegill" : {
				"desc" : "A small fish.",
				"xp" : 5,
				"level" : 1,
			},
			"minnow" : {
				"desc" : "A really small fish.",
				"xp" : 5,
				"level" : 1,
			},
		},
		"animals" : {
			"hare" : {
				"desc" : "A small hoppy creature.",
				"xp" : 5,
				"level" : 1,
			},
			"chicken" : {
				"desc" : "An edible dinosaur.",
				"xp" : 5,
				"level" : 1,
			},
		},
		"plants" : {
			"chamomile" : {
				"desc" : "A medicinal flower.",
				"xp" : 5,
				"level" : 1,
			},
			"tuber" : {
				"desc" : "Edible root material from a plant.",
				"xp" : 5,
				"level" : 1,
			},
		},
	},
}

enemies = {
	"goblin" : {
		"stats" : {
		},
		"desc" : "a common goblin",
	},
}