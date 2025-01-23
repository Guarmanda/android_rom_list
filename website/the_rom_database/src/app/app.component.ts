import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { AllCommunityModule, ColDef, GridApi, GridReadyEvent, ModuleRegistry } from 'ag-grid-community'; 
import { AgGridAngular } from 'ag-grid-angular'; // Angular Data Grid Component

ModuleRegistry.registerModules([AllCommunityModule]);

const RETAIL_BRANDING = "Retail Branding";
const MARKETING_NAME = "Marketing Name";
const CODE_NAME = "CodeName";
const MODEL = "Model";
const ROMS = "ROM(s) supporting device";
const NUMBER_OF_DEVICES = "Number of Devices";
const ROM = "ROM";

interface Device {
  [RETAIL_BRANDING]: string;
  [MARKETING_NAME]: string;
  [CODE_NAME]: string;
  [MODEL]: string;
  [ROMS]: string;
}

interface Rom {
  [ROM]: string;
  [NUMBER_OF_DEVICES]: number;
}

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, AgGridAngular],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {

  gridApi !: GridApi<Device>;
  title = 'the_rom_database';

  gridApi2 !: GridApi<Rom>;

  rowDataRaw: Device[] = [];
  romData2: Rom[] = [];

rowData: Device[] = [];

  onGridReady(params: GridReadyEvent<Device>) {
    this.gridApi = params.api;
    const baseHref = document.baseURI; // Retrieves the base href dynamically
    fetch(`${baseHref}data/supported_devices_with_roms.csv`)
    .then(response => response.text())
    .then(data => {
      let lines = data.split('\n');
      for (let i = 1; i < lines.length; i++) {
        console.log(lines[i]);
        let cols = lines[i].split(',');
        this.rowDataRaw.push({ [RETAIL_BRANDING]: cols[0], [MARKETING_NAME]: cols[1], [CODE_NAME]: cols[2], [MODEL]: cols[3], [ROMS]: cols[4] });
      }
      this.gridApi.setGridOption( 'rowData', this.rowDataRaw );
    });
  }

  onGridReady2(params: GridReadyEvent<Rom>) {
    this.gridApi2 = params.api;
    const baseHref = document.baseURI; // Retrieves the base href dynamically
    fetch(`${baseHref}data/rom_device_counts.csv`)
    .then(response => response.text())
    .then(data => {
      let lines = data.split('\n');
      for (let i = 1; i < lines.length; i++) {
        console.log(lines[i]);
        let cols = lines[i].split(',');
        this.romData2.push({ [ROM]: cols[0], [NUMBER_OF_DEVICES]: parseInt(cols[1]) });
      }
      this.gridApi2.setGridOption( 'rowData', this.romData2 );
    });
  }

// Column Definitions: Defines the columns to be displayed.
colDefs: ColDef[] = [
  { field: RETAIL_BRANDING, sortable: true, filter: true },
  { field: MARKETING_NAME, sortable: true, filter: true },
  { field: CODE_NAME, sortable: true, filter: true },
  { field: MODEL, sortable: true, filter: true },
  { field: ROMS, sortable: true, filter: true }
];

coldefs2: ColDef[] = [
  { field: ROM, sortable: true, filter: true },
  { field: NUMBER_OF_DEVICES, sortable: true, filter: true }
];
}
