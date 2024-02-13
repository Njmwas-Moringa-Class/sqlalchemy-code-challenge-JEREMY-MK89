"""Adjust review table

Revision ID: 0fb794a5a18b
Revises: 319fc88acaec
Create Date: 2024-02-14 00:18:15.447190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fb794a5a18b'
down_revision = '319fc88acaec'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add the 'comment' column to the 'reviews' table
    op.add_column('reviews', sa.Column('comment', sa.String(), nullable=True))



def downgrade() -> None:
    pass
