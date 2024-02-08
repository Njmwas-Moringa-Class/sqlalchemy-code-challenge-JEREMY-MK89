"""Create reviews table

Revision ID: effedd8d1e85
Revises: 2723e7bbcf91
Create Date: 2024-02-08 15:47:04.891230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'effedd8d1e85'
down_revision = '2723e7bbcf91'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Drop 'customers' table if it exists
    op.drop_table('customers', if_exists=True)

    # Drop 'restaurants' table if it exists
    op.drop_table('restaurants', if_exists=True)

    # ### end Alembic commands ###


def downgrade() -> None:
    # Create 'reviews' table
    op.create_table('reviews',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('star_rating', sa.Integer(), nullable=True),
        sa.Column('customer_id', sa.Integer(), nullable=True),
        sa.Column('restaurant_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
        sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    # Create 'restaurants' table
    op.create_table('restaurants',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('price', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Create 'customers' table
    op.create_table('customers',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(), nullable=True),
        sa.Column('last_name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # ### end Alembic commands ###
