#check the pop server for new messages
from poplib import *
import email

pop = POP3_SSL('mail.webfaction.com')

pop.user('brandon')
pop.pass_('jankcb3928')

pop.set_debuglevel(0)

mess = len(pop.list()[1])






