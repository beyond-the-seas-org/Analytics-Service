"""empty message

Revision ID: 171c10c81b88
Revises: 
Create Date: 2023-08-24 11:01:45.985908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '171c10c81b88'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('location',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('location_name', sa.String(length=50), nullable=False),
    sa.Column('country_name', sa.String(length=30), nullable=False),
    sa.Column('living_cost', sa.String(length=30), nullable=True),
    sa.Column('weather', sa.String(length=50), nullable=True),
    sa.Column('public_transportation', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('location')
    # ### end Alembic commands ###
