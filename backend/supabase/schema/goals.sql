CREATE TABLE goals (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id uuid REFERENCES users(id),
    title TEXT NOT NULL,
    description TEXT,
    target_date TIMESTAMP,
    progress INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT now()
);