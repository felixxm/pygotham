"""Add calls to action.

Revision ID: 62214735b8
Revises: 564d901de0c
Create Date: 2015-06-22 03:13:32.048821

"""

# revision identifiers, used by Alembic.
revision = '62214735b8'
down_revision = '564d901de0c'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('calls_to_action',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('url', sqlalchemy_utils.types.url.URLType(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('begins', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('ends', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], name=op.f('calls_to_action_event_id_fkey')),
    sa.PrimaryKeyConstraint('id', name=op.f('calls_to_action_pkey'))
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('calls_to_action')
    ### end Alembic commands ###