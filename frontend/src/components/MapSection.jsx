import { memo, useState } from "react";
import { ComposableMap, Geographies, Geography } from "react-simple-maps";

// Free public India states GeoJSON — no API key needed
const GEO_URL =
  "https://raw.githubusercontent.com/geohacker/india/master/state/india_telengana.geojson";

const HIGHLIGHTED = new Set([
  "Madhya Pradesh",
  "Rajasthan",
  "Haryana",
  "Punjab",
  "Uttar Pradesh",
  "Chhattisgarh",
  "Maharashtra",
]);

const OPERATE_LIST = [
  "Madhya Pradesh",
  "Rajasthan",
  "Haryana",
  "Punjab",
  "Uttar Pradesh",
  "Chhattisgarh",
  "Maharashtra",
];

const MapChart = memo(({ setTooltip }) => (
  <ComposableMap
    projection="geoMercator"
    projectionConfig={{ center: [82.9, 22.6], scale: 950 }}
    width={430}
    height={490}
    style={{ width: "100%", height: "auto" }}
  >
    <Geographies geography={GEO_URL}>
      {({ geographies }) =>
        geographies.map((geo) => {
          // handle different property name conventions in GeoJSON datasets
          const name =
            geo.properties.NAME_1 ||
            geo.properties.name ||
            geo.properties.ST_NM ||
            "";
          const isActive = HIGHLIGHTED.has(name);
          return (
            <Geography
              key={geo.rsmKey}
              geography={geo}
              onMouseEnter={() => isActive && setTooltip(name)}
              onMouseLeave={() => setTooltip("")}
              fill={isActive ? "#00563f" : "#deeede"}
              stroke={isActive ? "#004d38" : "#b5cdb5"}
              strokeWidth={0.6}
              style={{
                default: { outline: "none" },
                hover: {
                  fill: isActive ? "#007a58" : "#c8dfc8",
                  outline: "none",
                  cursor: isActive ? "pointer" : "default",
                },
                pressed: { outline: "none" },
              }}
            />
          );
        })
      }
    </Geographies>
  </ComposableMap>
));

export default function MapSection() {
  const [tooltip, setTooltip] = useState("");

  return (
    <section className="map-section-outer">
      <div className="map-section-inner">
        {/* Map */}
        <div className="map-svg-wrap">
          <div className="map-chart-wrap">
            <MapChart setTooltip={setTooltip} />
            {tooltip && <div className="map-tooltip-badge">{tooltip}</div>}
          </div>
          <div className="map-legend">
            <span>
              <span className="legend-dot leg-active" /> States We Operate In
            </span>
            <span>
              <span className="legend-dot leg-inactive" /> States We Don't Operate In
            </span>
          </div>
        </div>

        {/* Info panel */}
        <div className="map-info">
          <svg className="map-leaf-icon" width="30" height="30" viewBox="0 0 32 32" fill="none">
            <path d="M16 4C16 4 6 10 6 20c0 5.5 4.5 8 10 8s10-2.5 10-8C26 10 16 4 16 4z" fill="#00563f" opacity="0.18"/>
            <path d="M16 6C16 6 8 11.5 8 20c0 4.5 3.6 6.5 8 6.5s8-2 8-6.5C24 11.5 16 6 16 6z" fill="#00563f"/>
            <line x1="16" y1="28" x2="16" y2="14" stroke="#fff" strokeWidth="1.5" strokeLinecap="round"/>
          </svg>
          <h2 className="map-heading">
            States We<br />
            <span>Operate In</span>
          </h2>
          <p className="map-desc">
            AgriGem is proud to be present in{" "}
            <strong>seven key states</strong> across India, working closely with
            farmers and partners to drive growth and prosperity.
          </p>
          <div className="map-state-header">STATES WE OPERATE IN</div>
          <ul className="map-state-list">
            {OPERATE_LIST.map((state) => (
              <li key={state} className="map-state-item">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                  <path
                    d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"
                    fill="#00563f"
                  />
                </svg>
                {state}
              </li>
            ))}
          </ul>
        </div>
      </div>
    </section>
  );
}
