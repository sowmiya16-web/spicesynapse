export const TAGS = {
  eco_friendly: {
    label: 'Eco-Friendly',
    color: 'bg-green-100 text-green-700',
  },
  handmade: {
    label: 'Handmade',
    color: 'bg-yellow-100 text-yellow-700',
  },
  limited_edition: {
    label: 'Limited Edition',
    color: 'bg-red-100 text-red-700',
  },
  fair_trade: {
    label: 'Fair Trade',
    color: 'bg-blue-100 text-blue-700',
  },
  best_seller: {
    label: 'Best Seller',
    color: 'bg-purple-100 text-purple-700',
  }
};

export function getTagInfo(tagKey) {
  return TAGS[tagKey] || {
    label: tagKey,
    color: 'bg-gray-200 text-gray-800',
  };
}