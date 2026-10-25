export type Feature = {
  name: string;
  label: string;
  kind: 'number' | 'category';
  required: boolean;
  options?: string[];
  min?: number;
  max?: number;
};

const rating = (name: string): Feature =>
  ({ name, label: name, kind: 'number', required: true, min: 0, max: 5 });

// Exact names and order of the model's 22 raw inputs
export const FEATURES: Feature[] = [
  { name: 'Gender', label: 'Gender', kind: 'category', required: true,
    options: ['Male', 'Female'] },
  { name: 'Customer Type', label: 'Customer Type', kind: 'category', required: true,
    options: ['Loyal Customer', 'disloyal Customer'] },
  { name: 'Age', label: 'Age', kind: 'number', required: true, min: 5, max: 100 },
  { name: 'Type of Travel', label: 'Type of Travel', kind: 'category', required: true,
    options: ['Personal Travel', 'Business travel'] },
  { name: 'Class', label: 'Class', kind: 'category', required: true,
    options: ['Eco', 'Eco Plus', 'Business'] },
  { name: 'Flight Distance', label: 'Flight Distance (miles)', kind: 'number',
    required: true, min: 1, max: 6000 },
  rating('Inflight wifi service'),
  rating('Departure/Arrival time convenient'),
  rating('Ease of Online booking'),
  rating('Gate location'),
  rating('Food and drink'),
  rating('Online boarding'),
  rating('Seat comfort'),
  rating('Inflight entertainment'),
  rating('On-board service'),
  rating('Leg room service'),
  rating('Baggage handling'),
  rating('Checkin service'),
  rating('Inflight service'),
  rating('Cleanliness'),
  { name: 'Departure Delay in Minutes', label: 'Departure Delay (minutes)',
    kind: 'number', required: true, min: 0, max: 2000 },
  { name: 'Arrival Delay in Minutes', label: 'Arrival Delay (minutes)',
    kind: 'number', required: true, min: 0, max: 2000 },
];