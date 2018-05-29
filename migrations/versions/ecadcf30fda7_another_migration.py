"""another migration

Revision ID: ecadcf30fda7
Revises: 40a47307c6d3
Create Date: 2018-05-29 09:54:28.448974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecadcf30fda7'
down_revision = '40a47307c6d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'p_url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('p_url', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###