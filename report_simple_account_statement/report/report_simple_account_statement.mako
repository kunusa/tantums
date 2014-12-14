<html>
<head>
<style type="text/css">
	${css} 
</style>
</head>
<body>
<% setLang(user.lang) %>
<div>
		<div>
				<div>
		%if get_move_lines(data):
					${helper.embed_image('jpeg',str(get_move_lines(data)[0].company_id.logo_web),250, 120)}

				</div>
			<h3 class="title">
				${_('ACCOUNT SIMPLE STATEMENT REPORT') | entity}
				<%
				for (clave, valor) in data.items():
						print clave, ": ", valor
				%>
			</h3>
			<h5>
				<div align="center">
					<p>${_('FROM :')}${formatLang(get_move_lines(data)[0].date,date=True) | entity }</p>
					<p>${_('TO :')}${data['form']['date_finish']}</p>
				</div>
		%endif
			</h5>
		</div>
</div>

<table width="100%">
					<tr>
						<td width="12.5%" align='center'>
							${_('Document Date') | entity}	
						</td>
						<td width="12.5%" align='center'>
							${_('Document') | entity}
						</td>
						<td width="12.5%" align='center'>
							${_('Due Date') | entity}
						</td>
						<td width="12.5%" align='center'>
							${_('Journal') | entity}
						</td>
						<td width="12.5%" align='center'>
							${_('Currency') | entity}
						</td> 
						<td width="12.5%" align='center'>
							${_('Credit') | entity}
						</td>
						<td width="12.5%" align='center'>
							${_('Debit') | entity}
						</td>
						<td width="12.5%" align='center'>
							${_('Current Balance') | entity}
						</td>
					</tr>
					<tr>
    					<td colspan="8" align="right">
    						<font size='1'>
    				 			${_(' Last Balance') | entity} : ${formatLang(get_last_balance(data),monetary=True) or 0.00}
    				 		</font>
    				 	</td>
    				</tr>
</table>
    		
% for o in 	get_move_lines(data):
<table  width="100%">	
				%if (o.credit > 0):
					<tr>
							<td width="12.5%" align='center'>
								<font size="1">
									</div>${formatLang(o.date,date=True) | entity }</div>
								</font>
							</td>
							<td width="12.5%" align='center' style="font-zise:small;">
								<font size="1">
									${o.name}
								</font>
							</td>
							<td width="12.5%" align='center'>
								<font size="1">
								%if o.date_maturity: 
									${formatLang(o.date_maturity,date=True) | entity }
								%endif
								</font>
							</td>
							<td  width="12.5%" align='center'>
								<font size="1">
									${o.journal_id.code}
								</font>
							</td>
							<td width="12.5%" align='center'>
								<font size="1">
									##${o.currency_id.name}
								</font>
							</td>
							<td width="12.5%" align='center'>
								<font size="1">
									${formatLang(o.credit,monetary=True)}
								</font>
							</td>
							<td width="12.5%" align='center'>
								<font size="1">
								</font>

							</td>
							<td width="12.5%" align='center'>
								<font size="1">
								</font>		  	
							</td>
					</tr>
				%endif
				%if (o.debit > 0):
					 <tr>
						<td width="12.5%" align='center'>
							<font size="1">
								${formatLang(o.date,date=True)}
							</font>
						</td>
						<td width="12.5%" align='center'>
							<font size="1">
						    	${o.ref}
						    </font>
						</td>	
						<td width="12.5%" align='center'>
							##${payments_obj}
						</td>
						<td  width="12.5%" align='center'>
							<font size="1">
								${o.journal_id.code}
							</font>
						</td>	
						<td width="12.5%" align='center'>
							##${o.currency_id.name}
						</td>
						<td width="12.5%" align='center'>
							
						</td>
						<td width="12.5%" align='center'>
							<font size="1">
								${formatLang(o.debit,monetary=True)}
							</font>
						</td>
						</td>
						<td width="12.5%" align='center'>
							 ##${formatLang(residual,monetary=True)} 
						</td>
					</tr>
				%endif
%endfor
    				<tr>
	    				<td  colspan="3" align="left">
	    					<font size="1">
							<div width='12.5%'>${_('Charges')}${' : '}${formatLang(get_total_debit_credit(get_move_lines(data))['sum_tot_credit']) or '0.00' |entity}</div>
							</font>
						</td>
						<td  colspan="3" align="right">
							<font size="1">
								${_('Payments')}${' : '}${formatLang(get_total_debit_credit(get_move_lines(data))['sum_tot_debit']) or '0.00' |entity}
							</font>
						</td>
						<td  colspan="2" align="right">
							<font size="1">
								${_('Balance')}${' : '}${formatLang(get_total_debit_credit(get_move_lines(data))['sum_tot_credit']- get_total_debit_credit(get_move_lines(data))['sum_tot_debit']) or '0.00' |entity}
							</font>
						</td>
		</table>
			
<p style="page-break-before: always;"></p>
</body>
</html>