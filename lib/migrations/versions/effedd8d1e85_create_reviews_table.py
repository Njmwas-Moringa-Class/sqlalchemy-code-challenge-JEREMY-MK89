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

    # Create 'reviews' table with the 'comment' column
    op.create_table('reviews',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('comment', sa.String(), nullable=True),  # Add this line
        sa.Column('star_rating', sa.Integer(), nullable=True),
        sa.Column('customer_id', sa.Integer(), nullable=True),
        sa.Column('restaurant_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
        sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    # Recreate 'restaurants' table
    op.create_table('restaurants',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('price', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Recreate 'customers' table
    op.create_table('customers',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(), nullable=True),
        sa.Column('last_name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # ### end Alembic commands ###


def downgrade() -> None:
    # Recreate 'reviews' table without 'comment' column
    op.create_table('reviews',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('star_rating', sa.Integer(), nullable=True),
        sa.Column('customer_id', sa.Integer(), nullable=True),
        sa.Column('restaurant_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
        sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    # Recreate 'restaurants' table
    op.create_table('restaurants',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('price', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Recreate 'customers' table
    op.create_table('customers',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(), nullable=True),
        sa.Column('last_name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # ### end Alembic commands ###
